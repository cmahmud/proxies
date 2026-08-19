# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 501
- HTTP: 386 alive / 165 gold
- HTTPS: 235 alive / 93 gold
- SOCKS4: 193 alive / 110 gold
- SOCKS5: 234 alive / 133 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18769
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
