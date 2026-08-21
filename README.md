# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 437
- HTTP: 314 alive / 113 gold
- HTTPS: 229 alive / 28 gold
- SOCKS4: 235 alive / 154 gold
- SOCKS5: 233 alive / 142 gold

## Historical pool

- Discovered: 160020
- Ever alive: 30532
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
