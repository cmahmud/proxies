# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 420
- HTTP: 105 alive / 76 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49452
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
