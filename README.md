# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 380
- HTTP: 103 alive / 54 gold
- HTTPS: 36 alive / 8 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 191 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33435
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
