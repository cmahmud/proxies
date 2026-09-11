# SyndProxy validated proxy pool

## Current pool

- Alive now: 684
- Gold now: 333
- HTTP: 149 alive / 77 gold
- HTTPS: 105 alive / 33 gold
- SOCKS4: 101 alive / 53 gold
- SOCKS5: 329 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48554
- Ever gold: 1545

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
