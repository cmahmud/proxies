# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 446
- HTTP: 148 alive / 82 gold
- HTTPS: 104 alive / 30 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 216 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45446
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
