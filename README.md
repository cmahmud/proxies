# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 406
- HTTP: 184 alive / 85 gold
- HTTPS: 153 alive / 24 gold
- SOCKS4: 210 alive / 154 gold
- SOCKS5: 224 alive / 143 gold

## Historical pool

- Discovered: 149522
- Ever alive: 26992
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
