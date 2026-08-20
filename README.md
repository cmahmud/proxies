# SyndProxy private pool

## Current pool

- Alive now: 736
- Gold now: 355
- HTTP: 197 alive / 63 gold
- HTTPS: 138 alive / 17 gold
- SOCKS4: 198 alive / 132 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 145551
- Ever alive: 25419
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
