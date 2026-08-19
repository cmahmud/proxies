# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 533
- HTTP: 417 alive / 159 gold
- HTTPS: 274 alive / 87 gold
- SOCKS4: 238 alive / 157 gold
- SOCKS5: 203 alive / 130 gold

## Historical pool

- Discovered: 119819
- Ever alive: 18183
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
