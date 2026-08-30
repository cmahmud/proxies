# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 427
- HTTP: 140 alive / 87 gold
- HTTPS: 88 alive / 28 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 209 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43988
- Ever gold: 1387

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
