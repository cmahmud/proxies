# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 438
- HTTP: 238 alive / 92 gold
- HTTPS: 186 alive / 31 gold
- SOCKS4: 226 alive / 151 gold
- SOCKS5: 256 alive / 164 gold

## Historical pool

- Discovered: 163279
- Ever alive: 31811
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
