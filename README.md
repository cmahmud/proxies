# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 415
- HTTP: 110 alive / 67 gold
- HTTPS: 83 alive / 20 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35377
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
