# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 456
- HTTP: 127 alive / 88 gold
- HTTPS: 115 alive / 35 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 201 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44791
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
