# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 384
- HTTP: 107 alive / 54 gold
- HTTPS: 49 alive / 11 gold
- SOCKS4: 181 alive / 158 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33478
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
