FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["as-net-core-page/as-net-core-page.csproj", "as-net-core-page/"]
RUN dotnet restore "as-net-core-page/as-net-core-page.csproj"
COPY . .
WORKDIR "src/as-net-core-page"
RUN dotnet build "as-net-core-page.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "as-net-core-page.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "as-net-core-page.dll"]