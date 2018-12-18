FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ./asp-net-core-page.csproj .
RUN dotnet restore asp-net-core-page.csproj
COPY . .
RUN dotnet build asp-net-core-page.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish asp-net-core-page.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "asp-net-core-page.dll"]