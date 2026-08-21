# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 391
- HTTP: 298 alive / 77 gold
- HTTPS: 223 alive / 20 gold
- SOCKS4: 230 alive / 143 gold
- SOCKS5: 239 alive / 151 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29570
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
