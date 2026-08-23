# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 361
- HTTP: 70 alive / 40 gold
- HTTPS: 32 alive / 9 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33020
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
