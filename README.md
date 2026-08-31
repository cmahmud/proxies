# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 450
- HTTP: 142 alive / 82 gold
- HTTPS: 100 alive / 34 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 220 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45434
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
