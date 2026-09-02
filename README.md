# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 442
- HTTP: 94 alive / 69 gold
- HTTPS: 97 alive / 33 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 186 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47499
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
