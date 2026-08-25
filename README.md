# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 415
- HTTP: 97 alive / 65 gold
- HTTPS: 99 alive / 20 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35528
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
