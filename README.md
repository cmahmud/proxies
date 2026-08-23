# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 360
- HTTP: 80 alive / 41 gold
- HTTPS: 33 alive / 9 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 186 alive / 156 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33015
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
