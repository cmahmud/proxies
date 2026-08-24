# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 443
- HTTP: 123 alive / 83 gold
- HTTPS: 75 alive / 26 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 182 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34719
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
