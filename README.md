# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 414
- HTTP: 123 alive / 72 gold
- HTTPS: 61 alive / 20 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33746
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
