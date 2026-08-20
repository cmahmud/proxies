# SyndProxy private pool

## Current pool

- Alive now: 674
- Gold now: 384
- HTTP: 168 alive / 60 gold
- HTTPS: 77 alive / 18 gold
- SOCKS4: 216 alive / 152 gold
- SOCKS5: 213 alive / 154 gold

## Historical pool

- Discovered: 146660
- Ever alive: 25716
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
