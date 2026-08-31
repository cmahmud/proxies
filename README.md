# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 477
- HTTP: 144 alive / 103 gold
- HTTPS: 114 alive / 38 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45087
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
