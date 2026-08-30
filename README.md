# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 440
- HTTP: 123 alive / 79 gold
- HTTPS: 135 alive / 33 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44716
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
