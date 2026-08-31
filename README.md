# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 480
- HTTP: 135 alive / 103 gold
- HTTPS: 115 alive / 43 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45078
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
