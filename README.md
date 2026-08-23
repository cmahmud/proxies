# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 345
- HTTP: 139 alive / 40 gold
- HTTPS: 65 alive / 9 gold
- SOCKS4: 175 alive / 154 gold
- SOCKS5: 197 alive / 142 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32880
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
