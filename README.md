# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 440
- HTTP: 88 alive / 69 gold
- HTTPS: 90 alive / 30 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47466
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
