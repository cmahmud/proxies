# SyndProxy private pool

## Current pool

- Alive now: 948
- Gold now: 300
- HTTP: 335 alive / 63 gold
- HTTPS: 225 alive / 19 gold
- SOCKS4: 194 alive / 113 gold
- SOCKS5: 194 alive / 105 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15491
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
