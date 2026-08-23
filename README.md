# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 360
- HTTP: 78 alive / 42 gold
- HTTPS: 31 alive / 9 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 184 alive / 155 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33015
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
