# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 439
- HTTP: 88 alive / 72 gold
- HTTPS: 105 alive / 30 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47492
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
