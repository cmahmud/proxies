# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 452
- HTTP: 128 alive / 82 gold
- HTTPS: 89 alive / 36 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 223 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45356
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
