# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 470
- HTTP: 137 alive / 95 gold
- HTTPS: 114 alive / 42 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 199 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44914
- Ever gold: 1418

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
