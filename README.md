# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 450
- HTTP: 111 alive / 85 gold
- HTTPS: 98 alive / 32 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45646
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
