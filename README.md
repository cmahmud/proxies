# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 428
- HTTP: 143 alive / 87 gold
- HTTPS: 88 alive / 28 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 208 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43990
- Ever gold: 1387

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
