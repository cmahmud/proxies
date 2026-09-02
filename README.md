# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 445
- HTTP: 85 alive / 73 gold
- HTTPS: 124 alive / 32 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 184 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47485
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
