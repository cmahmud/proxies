# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 409
- HTTP: 116 alive / 64 gold
- HTTPS: 77 alive / 16 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38413
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
