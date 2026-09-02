# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 445
- HTTP: 93 alive / 73 gold
- HTTPS: 111 alive / 32 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47481
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
