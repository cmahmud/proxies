# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 394
- HTTP: 315 alive / 76 gold
- HTTPS: 202 alive / 23 gold
- SOCKS4: 226 alive / 144 gold
- SOCKS5: 246 alive / 151 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29570
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
