# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 440
- HTTP: 91 alive / 70 gold
- HTTPS: 95 alive / 30 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 188 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47488
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
