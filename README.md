# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 407
- HTTP: 91 alive / 64 gold
- HTTPS: 106 alive / 17 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41440
- Ever gold: 1330

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
