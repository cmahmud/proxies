# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 417
- HTTP: 92 alive / 63 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36125
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
