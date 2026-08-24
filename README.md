# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 389
- HTTP: 143 alive / 54 gold
- HTTPS: 34 alive / 15 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 196 alive / 162 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33601
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
