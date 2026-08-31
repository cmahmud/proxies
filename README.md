# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 445
- HTTP: 111 alive / 84 gold
- HTTPS: 63 alive / 29 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 201 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45566
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
