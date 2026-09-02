# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 437
- HTTP: 93 alive / 70 gold
- HTTPS: 96 alive / 30 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47490
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
