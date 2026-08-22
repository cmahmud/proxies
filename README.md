# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 443
- HTTP: 234 alive / 96 gold
- HTTPS: 176 alive / 32 gold
- SOCKS4: 233 alive / 151 gold
- SOCKS5: 265 alive / 164 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31806
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
