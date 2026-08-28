# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 429
- HTTP: 106 alive / 77 gold
- HTTPS: 129 alive / 20 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42443
- Ever gold: 1356

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
