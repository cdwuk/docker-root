FROM microsoft/aspnetcore:2.0 AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/aspnetcore-build:2.0 AS build
WORKDIR /src
COPY ["asp-net-core-linux-backend/asp-net-core-linux-backend.csproj", "asp-net-core-linux-backend/"]
RUN dotnet restore "asp-net-core-linux-backend/asp-net-core-linux-backend.csproj"
COPY . .
WORKDIR "/src/asp-net-core-linux-backend"
RUN dotnet build "asp-net-core-linux-backend.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "asp-net-core-linux-backend.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "asp-net-core-linux-backend.dll"]