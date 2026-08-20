# SyndProxy private pool

## Current pool

- Alive now: 759
- Gold now: 410
- HTTP: 187 alive / 87 gold
- HTTPS: 143 alive / 26 gold
- SOCKS4: 216 alive / 154 gold
- SOCKS5: 213 alive / 143 gold

## Historical pool

- Discovered: 149523
- Ever alive: 26995
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
