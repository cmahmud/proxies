# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 444
- HTTP: 92 alive / 72 gold
- HTTPS: 112 alive / 32 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47481
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
