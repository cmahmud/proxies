# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 457
- HTTP: 129 alive / 89 gold
- HTTPS: 109 alive / 35 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44793
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
