# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 479
- HTTP: 137 alive / 101 gold
- HTTPS: 126 alive / 41 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45093
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
