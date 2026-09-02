# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 445
- HTTP: 91 alive / 72 gold
- HTTPS: 115 alive / 33 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47482
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
